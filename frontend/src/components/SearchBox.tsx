"use client";

type Props = {
  topic: string;
  setTopic: (value: string) => void;
  onSearch: () => void;
  loading: boolean;
};

export default function SearchBox({
  topic,
  setTopic,
  onSearch,
  loading,
}: Props) {
  return (
    <div className="w-full max-w-3xl">
      <input
        className="w-full rounded-xl border border-gray-700 bg-gray-900 p-4 text-white"
        placeholder="Enter a research topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button
        onClick={onSearch}
        className="mt-4 w-full rounded-xl bg-blue-600 p-4 hover:bg-blue-700"
      >
        {loading ? "Researching..." : "Start Research"}
      </button>
    </div>
  );
}