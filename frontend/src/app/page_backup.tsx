"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { research } from "@/lib/api";

export default function Home() {
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState("");

  async function handleResearch() {
    if (!topic.trim()) return;

    setLoading(true);

    try {
      const data = await research(topic);
      setReport(data.report ?? JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center p-8">
      <h1 className="text-5xl font-bold mb-8">Prometheus-X</h1>

      <input
        className="w-full max-w-2xl rounded-lg border border-gray-700 bg-gray-900 p-4"
        placeholder="Enter research topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button
        onClick={handleResearch}
        className="mt-4 rounded-lg bg-blue-600 px-6 py-3 hover:bg-blue-700"
      >
        {loading ? "Researching..." : "Start Research"}
      </button>

      {loading && (
        <div className="mt-6 text-blue-400 animate-pulse">
          🔍 Researching... Please wait.
        </div>
      )}

      {report && (
        <div className="mt-8 w-full max-w-5xl rounded-xl bg-gray-900 p-8">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {report}
          </ReactMarkdown>
        </div>
      )}
    </main>
  );
}
