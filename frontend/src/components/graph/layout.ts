import type { TopicNode,TopicEdge } from "../../types";
interface PositionedNode {
  id: string;
  type: string;
  data: { label: string; completed: boolean; onToggle: () => void };
  position: { x: number; y: number };
}

interface PositionedEdge {
    id: string;
    source: string;
    target: string;
}

const COLUMN_WIDTH = 280;
const ROW_HEIGHT = 100;

export function computeLayout(
  nodes: TopicNode[],
  edges: TopicEdge[],
  completedNodeIds: Set<number>,
  onToggle: (nodeId: number) => void
): { flowNodes: PositionedNode[]; flowEdges: PositionedEdge[] } {
    const prerequisitesOf = new Map<number,number[]>();
    nodes.forEach((n)=>prerequisitesOf.set(n.id,[]));
    edges.forEach((e)=>{
        prerequisitesOf.get(e.target_node_id)?.push(e.source_node_id);
    });

    const levelCache = new Map<number,number>();
    function levelOf(nodeId: number, visiting = new Set<number>()): number {
        if( levelCache.has(nodeId)) return levelCache.get(nodeId)!;
        if( visiting.has(nodeId)) return 0;
        visiting.add(nodeId);
        const prereqs = prerequisitesOf.get(nodeId) ?? [];
        const level = prereqs.length===0
            ? 0
            :1 +Math.max(...prereqs.map((p)=> levelOf(p,visiting)));
    
        levelCache.set(nodeId,level);
        return level;
    }

    nodes.forEach((n)=>levelOf(n.id));

    const nodesByLevel = new Map<number, number[]>();
    nodes.forEach((n)=>{
        const level = levelCache.get(n.id)!;
        if (!nodesByLevel.has(level)) nodesByLevel.set(level,[]);
        nodesByLevel.get(level)!.push(n.id);
    });

    const flowNodes: PositionedNode[] = nodes.map((n) => {
    const level = levelCache.get(n.id)!;
    const column = nodesByLevel.get(level)!;
    const rowIndex = column.indexOf(n.id);

    return {
      id: String(n.id),
      type: 'topic',
      data: {
        label: n.title,
        completed: completedNodeIds.has(n.id),
        onToggle: () => onToggle(n.id),
      },
      position: {
        x: level * COLUMN_WIDTH,
        y: rowIndex * ROW_HEIGHT,
      },
    };
  });

    const flowEdges: PositionedEdge[] = edges.map((e)=>({
        id: `e${e.id}`,
        source: String(e.source_node_id),
        target: String(e.target_node_id),
    }));

    return {flowNodes,flowEdges};
}