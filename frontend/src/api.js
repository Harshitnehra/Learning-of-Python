
const BASE = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '')


export const api = {
  employees: `${BASE}/api/employees/`,
  attendance: `${BASE}/api/attendance/`,
  health: `${BASE}/api/health`,
}

/**
 * Check if backend is reachable.
 * @returns {Promise<{ ok: boolean, message?: string }>}
 */
export async function checkBackendConnection() {
  try {
    const res = await fetch(api.health, { method: 'GET' })
    if (res.ok) return { ok: true }
    return { ok: false, message: `Backend returned ${res.status}` }
  } catch (e) {
    return { ok: false, message: e.message || '' }
  }
}

export async function fetchApi(url, options = {}) {
  const res = await fetch(url, {
    ...options,
    headers: { 'Content-Type': 'application/json', ...options.headers },
  })
  const data = await res.json().catch(() => ({}))
  if (!res.ok) {
    const err = new Error(data.detail || res.statusText)
    err.status = res.status
    err.data = data
    throw err
  }
  return data
}
