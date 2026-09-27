import ReactFlow, { Background, Controls, MiniMap } from 'reactflow';
import 'reactflow/dist/style.css';
import { useCurriculumGraph, useProgress, useUpdateProgress, useCoverage } from '../api/client';
import { computeLayout } from '../components/graph/layout';
import { TopicNode } from '../components/graph/TopicNode';

const nodeTypes = { topic: TopicNode };

interface RoadmapViewerProps {
  curriculumId: number;
}

export function RoadmapViewer({ curriculumId }: RoadmapViewerProps) {
  const { data, isLoading, error } = useCurriculumGraph(curriculumId);
  const { data: progressData } = useProgress(curriculumId);
  const { data: coverage } = useCoverage(curriculumId);
  const updateProgress = useUpdateProgress(curriculumId);

  if (isLoading) return <p>Loading roadmap...</p>;
  if (error) return <p>Error: {error.message}</p>;
  if (!data) return null;

  const completedNodeIds = new Set(
    (progressData ?? []).filter((p) => p.completed).map((p) => p.node_id)
  );

  const handleToggle = (nodeId: number) => {
    const isCurrentlyCompleted = completedNodeIds.has(nodeId);
    updateProgress.mutate({ nodeId, completed: !isCurrentlyCompleted });
  };

  const { flowNodes, flowEdges } = computeLayout(data.nodes, data.edges, completedNodeIds, handleToggle);

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <div style={{ padding: '1rem', display: 'flex', justifyContent: 'space-between' }}>
        <h2>{data.name}</h2>
        {coverage && (
          <p style={{ fontWeight: 600 }}>
            {coverage.completed_nodes}/{coverage.total_nodes} completed ({coverage.percentage}%)
          </p>
        )}
      </div>
      <div style={{ width: '100%', height: 'calc(100% - 60px)' }}>
        <ReactFlow nodes={flowNodes} edges={flowEdges} nodeTypes={nodeTypes} fitView>
          <Background />
          <Controls />
          <MiniMap />
        </ReactFlow>
      </div>
    </div>
  );
}