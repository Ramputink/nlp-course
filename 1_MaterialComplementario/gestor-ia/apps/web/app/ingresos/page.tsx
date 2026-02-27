"use client";

import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";

const invoices = [
  { id: 1, client: "Cliente Uno", date: "2025-12-02", total: 1500, vat: 315 },
  { id: 2, client: "Cliente Dos", date: "2025-12-15", total: 950, vat: 199.5 },
];

export default function IngresosPage() {
  return (
    <AppShell>
      <TopBar title="Ingresos / Facturas" subtitle="Crear factura y exportar (mock)" />
      <div className="card">
        <div className="flex justify-between items-center">
          <h3 className="text-xl font-display">Facturas</h3>
          <button className="px-3 py-2 rounded-xl bg-black text-white">
            Crear factura
          </button>
        </div>
        <div className="mt-4 space-y-3">
          {invoices.map((inv) => (
            <div key={inv.id} className="p-3 border rounded-xl bg-white">
              <div className="flex justify-between">
                <div>
                  <div className="font-semibold">{inv.client}</div>
                  <div className="text-sm text-black/60">{inv.date}</div>
                </div>
                <div className="text-right">
                  <div className="font-semibold">{inv.total} EUR</div>
                  <div className="text-sm text-black/60">IVA {inv.vat} EUR</div>
                </div>
              </div>
              <button className="mt-2 text-sm underline">Export PDF (mock)</button>
            </div>
          ))}
        </div>
      </div>
    </AppShell>
  );
}
