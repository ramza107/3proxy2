import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { prisma } from "@/lib/prisma";

const ROLES = new Set(["founder", "partner", "both"]);

export async function POST(request: Request) {
  let body: { email?: string; password?: string; role?: string };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "invalid_json" }, { status: 400 });
  }

  const email = body.email?.toLowerCase().trim();
  const password = body.password;
  const role = body.role ?? "founder";

  if (!email || !password) {
    return NextResponse.json({ error: "missing_fields" }, { status: 400 });
  }

  if (password.length < 8) {
    return NextResponse.json({ error: "password_short" }, { status: 400 });
  }

  if (!ROLES.has(role)) {
    return NextResponse.json({ error: "invalid_role" }, { status: 400 });
  }

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return NextResponse.json({ error: "email_taken" }, { status: 409 });
  }

  const passwordHash = await bcrypt.hash(password, 12);

  const user = await prisma.user.create({
    data: { email, passwordHash, role },
  });

  return NextResponse.json({
    id: user.id,
    email: user.email,
  });
}
