export function ChatBubble({
  role,
  text,
}: {
  role: "user" | "system";
  text: string;
}) {
  const isUser = role === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[70%] px-4 py-3 rounded-2xl ${
          isUser ? "bg-[#0a3d62] text-white" : "bg-white text-black border"
        }`}
      >
        {text}
      </div>
    </div>
  );
}
