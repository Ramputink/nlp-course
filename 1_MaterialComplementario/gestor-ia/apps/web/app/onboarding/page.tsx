"use client";

import { useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function OnboardingPage() {
  const [email, setEmail] = useState("ana@autonomos.es");
  const [token, setToken] = useState("");
  const [status, setStatus] = useState("");
  const [profile, setProfile] = useState({
    provincia: "Madrid",
    regimen_autonomo: "Estimacion directa",
    actividad: "Consultoria",
    start_date: "2021-01-01",
    retention_days: 365,
  });

  const sendMagic = async () => {
    const res = await fetch(`${API_URL}/auth/magic-link`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    });
    const data = await res.json();
    setToken(data.token);
    setStatus(`Magic link enviado (mock): ${data.preview_url}`);
  };

  const verify = async () => {
    const res = await fetch(`${API_URL}/auth/verify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, token }),
    });
    const data = await res.json();
    setStatus(`Autenticado. user_id=${data.user_id}`);
  };

  const saveProfile = async () => {
    await fetch(`${API_URL}/profile/1`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile),
    });
    setStatus("Perfil guardado.");
  };

  return (
    <AppShell>
      <TopBar title="Onboarding" subtitle="Crear cuenta y perfil" />
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-xl font-display mb-3">Crear cuenta (email)</h3>
          <input
            className="w-full px-3 py-2 border rounded-xl"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <div className="mt-3 flex gap-3">
            <button className="px-3 py-2 rounded-xl bg-black text-white" onClick={sendMagic}>
              Enviar magic link
            </button>
            <button className="px-3 py-2 rounded-xl border" onClick={verify}>
              Verificar
            </button>
          </div>
        </div>
        <div className="card">
          <h3 className="text-xl font-display mb-3">Crear perfil</h3>
          <div className="space-y-2">
            {Object.entries(profile).map(([key, value]) => (
              <input
                key={key}
                className="w-full px-3 py-2 border rounded-xl"
                value={value as any}
                onChange={(e) =>
                  setProfile({ ...profile, [key]: e.target.value })
                }
                placeholder={key}
              />
            ))}
          </div>
          <button className="mt-3 px-3 py-2 rounded-xl bg-black text-white" onClick={saveProfile}>
            Guardar perfil
          </button>
        </div>
      </div>
      {status && <div className="mt-4 text-sm text-black/70">{status}</div>}
    </AppShell>
  );
}
