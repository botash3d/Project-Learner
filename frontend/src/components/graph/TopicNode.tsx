import { Handle, Position } from 'reactflow';

interface TopicNodeProps {
  data: {
    label: string;
    completed: boolean;
    onToggle: () => void;
  };
}

export function TopicNode({ data }: TopicNodeProps) {
    console.log(data.label, data.completed);

  return (
    <div
      onClick={data.onToggle}
      className={`rounded-lg border-2 px-4 py-3 shadow-md min-w-[180px] cursor-pointer transition-colors ${
        data.completed
          ? 'bg-green-100 border-green-500'
          : 'bg-white border-blue-400'
      }`}
    >
      <Handle type="target" position={Position.Left} className="!bg-blue-400" />
      <p className="text-sm font-semibold text-gray-800">
        {data.completed ? '✅ ' : ''}{data.label}
      </p>
      <Handle type="source" position={Position.Right} className="!bg-blue-400" />
    </div>
  );
}