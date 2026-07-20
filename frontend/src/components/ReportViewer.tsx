import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function ReportViewer({
  report,
}: {
  report: string;
}) {
  if (!report) return null;

  return (
    <div className="mt-8 max-w-5xl rounded-xl bg-gray-900 p-8 text-white">
      <ReactMarkdown remarkPlugins={[remarkGfm]}>
        {report}
      </ReactMarkdown>
    </div>
  );
}