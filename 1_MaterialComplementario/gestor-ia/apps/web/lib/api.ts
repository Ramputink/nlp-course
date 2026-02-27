const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function getExpenses(userId: number) {
  const res = await fetch(`${API_URL}/expenses?user_id=${userId}`, {
    cache: "no-store",
  });
  return res.json();
}

export async function getAlerts(userId: number) {
  const res = await fetch(`${API_URL}/alerts?user_id=${userId}`, {
    cache: "no-store",
  });
  return res.json();
}

export async function getWhatsappEvents(userId: number) {
  const res = await fetch(`${API_URL}/whatsapp/events?user_id=${userId}`, {
    cache: "no-store",
  });
  return res.json();
}

export async function sendWhatsappMessage(userId: number, text: string) {
  const res = await fetch(`${API_URL}/whatsapp/emulator`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, type: "text", text }),
  });
  return res.json();
}

export async function askRag(userId: number, question: string) {
  const res = await fetch(`${API_URL}/rag/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, question }),
  });
  return res.json();
}

export async function getSource(sourceId: number, q: string) {
  const res = await fetch(`${API_URL}/sources/${sourceId}?q=${encodeURIComponent(q)}`, {
    cache: "no-store",
  });
  return res.json();
}

export async function getFilings(userId: number) {
  const res = await fetch(`${API_URL}/filings?user_id=${userId}`, {
    cache: "no-store",
  });
  return res.json();
}

export async function getPartnerReviews(partnerId: number) {
  const res = await fetch(`${API_URL}/partners/reviews?partner_user_id=${partnerId}`, {
    cache: "no-store",
  });
  return res.json();
}
