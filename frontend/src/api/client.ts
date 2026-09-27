import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import type { CurriculumGraph } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function fetchCurriculumGraph(curriculumId: number): Promise<CurriculumGraph> {
  const response = await fetch(`${API_BASE_URL}/api/curricula/${curriculumId}/graph`);
  if (!response.ok) throw new Error(`Failed to fetch curriculum graph: ${response.status}`);
  return response.json();
}

export function useCurriculumGraph(curriculumId: number) {
  return useQuery({
    queryKey: ['curriculumGraph', curriculumId],
    queryFn: () => fetchCurriculumGraph(curriculumId),
  });
}

export interface ProgressEntry {
  node_id: number;
  completed: boolean;
}

async function fetchProgress(curriculumId: number): Promise<ProgressEntry[]> {
  const response = await fetch(`${API_BASE_URL}/api/curricula/${curriculumId}/progress`);
  if (!response.ok) throw new Error(`Failed to fetch progress: ${response.status}`);
  return response.json();
}

export function useProgress(curriculumId: number) {
  return useQuery({
    queryKey: ['progress', curriculumId],
    queryFn: () => fetchProgress(curriculumId),
  });
}

async function updateNodeProgress(nodeId: number, completed: boolean) {
  const response = await fetch(`${API_BASE_URL}/api/progress/${nodeId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ completed }),
  });
  if (!response.ok) throw new Error(`Failed to update progress: ${response.status}`);
  return response.json();
}

export function useUpdateProgress(curriculumId: number) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ nodeId, completed }: { nodeId: number; completed: boolean }) =>
      updateNodeProgress(nodeId, completed),
    onSuccess: () => {
      // Refetch progress and coverage after a successful update
      queryClient.invalidateQueries({ queryKey: ['progress', curriculumId] });
      queryClient.invalidateQueries({ queryKey: ['coverage', curriculumId] });
    },
  });
}

export interface Coverage {
  curriculum_id: number;
  total_nodes: number;
  completed_nodes: number;
  percentage: number;
}

async function fetchCoverage(curriculumId: number): Promise<Coverage> {
  const response = await fetch(`${API_BASE_URL}/api/curricula/${curriculumId}/coverage`);
  if (!response.ok) throw new Error(`Failed to fetch coverage: ${response.status}`);
  return response.json();
}

export function useCoverage(curriculumId: number) {
  return useQuery({
    queryKey: ['coverage', curriculumId],
    queryFn: () => fetchCoverage(curriculumId),
  });
}