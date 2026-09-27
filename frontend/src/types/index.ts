export interface TopicNode {
  id: number;
  title: string;
  description: string | null;
}

export interface TopicEdge {
  id: number;
  source_node_id: number;
  target_node_id: number;
}

export interface CurriculumGraph {
  id: number;
  name: string;
  description: string | null;
  nodes: TopicNode[];
  edges: TopicEdge[];
}