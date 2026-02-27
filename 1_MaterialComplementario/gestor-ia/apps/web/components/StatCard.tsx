export function StatCard({
  title,
  value,
  footnote,
}: {
  title: string;
  value: string;
  footnote?: string;
}) {
  return (
    <div className="card">
      <div className="text-sm uppercase tracking-wide text-black/60">{title}</div>
      <div className="text-3xl font-display mt-2">{value}</div>
      {footnote && <div className="text-sm text-black/60 mt-2">{footnote}</div>}
    </div>
  );
}
