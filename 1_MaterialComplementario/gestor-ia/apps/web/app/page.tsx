"use client";

import { useState } from "react";
import Link from "next/link";

export default function LandingPage() {
  const [values, setValues] = useState([1200, 850, 430]);
  const total = values.reduce((a, b) => a + b, 0);
  const iva = total * 0.21;
  const irpf = total * 0.15;

  return (
    <div className="min-h-screen px-10 py-16">
      <header className="flex items-center justify-between">
        <div className="text-3xl font-display font-semibold">Gestor.ia</div>
        <div className="flex gap-4">
          <Link className="text-sm underline" href="/dashboard">
            Ir al MVP
          </Link>
        </div>
      </header>

      <section className="mt-16 grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
        <div>
          <h1 className="text-5xl font-display font-semibold">
            Zero-admin para autonomos en Espana
          </h1>
          <p className="mt-4 text-lg text-black/70">
            Copilot fiscal con RAG gov-only y WhatsApp simulado. Recibe tus
            gastos, entiende notificaciones DEHU y prepara borradores con citas
            verificables.
          </p>
          <div className="mt-6 flex gap-3">
            <Link
              href="/dashboard"
              className="px-5 py-3 rounded-xl bg-black text-white"
            >
              Probar MVP
            </Link>
            <button className="px-5 py-3 rounded-xl border border-black/10">
              Ver planes
            </button>
          </div>
        </div>

        <div className="card">
          <h2 className="text-2xl font-display">Susto calculator</h2>
          <p className="text-sm text-black/60">
            Sube 3 facturas (mock) y estima IVA/IRPF. Solo orientativo.
          </p>
          <div className="mt-4 space-y-3">
            {values.map((v, i) => (
              <input
                key={i}
                type="number"
                value={v}
                className="w-full px-3 py-2 border rounded-lg"
                onChange={(e) => {
                  const next = [...values];
                  next[i] = Number(e.target.value || 0);
                  setValues(next);
                }}
              />
            ))}
          </div>
          <div className="mt-5 p-4 rounded-xl bg-white border">
            <div className="text-sm text-black/60">Total facturado</div>
            <div className="text-2xl font-display">{total.toFixed(2)} EUR</div>
            <div className="mt-2 text-sm text-black/60">
              IVA estimado: {iva.toFixed(2)} EUR
            </div>
            <div className="text-sm text-black/60">
              IRPF estimado: {irpf.toFixed(2)} EUR
            </div>
          </div>
          <p className="text-xs text-black/50 mt-3">
            Disclaimer: estimaciones mock, no sustituyen asesoramiento profesional.
          </p>
        </div>
      </section>
    </div>
  );
}
