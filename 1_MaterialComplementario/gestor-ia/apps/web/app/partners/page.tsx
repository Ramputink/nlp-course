"use client";

import { useEffect, useState } from "react";
import { AppShell } from "@/components/AppShell";
import { TopBar } from "@/components/TopBar";
import { getPartnerReviews, getFilings } from "@/lib/api";

export default function PartnersPage() {
  const [reviews, setReviews] = useState<any[]>([]);
  const [filings, setFilings] = useState<any[]>([]);
  const partnerId = 2;
  const userId = 1;

  useEffect(() => {
    getPartnerReviews(partnerId).then(setReviews);
    getFilings(userId).then(setFilings);
  }, []);

  return (
    <AppShell>
      <TopBar title="Partners" subtitle="Revision humana con SLA" />
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-xl font-display mb-3">Solicitar revision</h3>
          <div className="space-y-3">
            {filings.map((f) => (
              <div key={f.id} className="p-3 border rounded-xl bg-white">
                <div className="font-semibold">{f.model} - {f.period}</div>
                <div className="text-sm text-black/60">Estado: {f.status}</div>
                <button className="mt-2 text-sm underline">Solicitar revision (mock)</button>
              </div>
            ))}
          </div>
        </div>
        <div className="card">
          <h3 className="text-xl font-display mb-3">Cola partner_gestor</h3>
          <div className="space-y-3">
            {reviews.map((r) => (
              <div key={r.id} className="p-3 border rounded-xl bg-white">
                <div className="font-semibold">Filing #{r.filing_id}</div>
                <div className="text-sm text-black/60">Estado: {r.status}</div>
                <button className="mt-2 text-sm underline">Aprobar (mock)</button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </AppShell>
  );
}
