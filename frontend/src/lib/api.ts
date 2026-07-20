const API_URL = "http://127.0.0.1:8000";

export async function research(topic: string) {
  const response = await fetch(
    `${API_URL}/research?topic=${encodeURIComponent(topic)}`
  );

  if (!response.ok) {
    throw new Error("Failed to generate research");
  }

  return response.json();
}