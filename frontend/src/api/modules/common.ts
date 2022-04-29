import client from '@/api/client';

export const healthCheck = async () => client.get('/health-check');
