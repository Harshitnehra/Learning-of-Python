import { useState, useEffect } from 'react'
import { api, fetchApi } from '../api'

function formatDate(val) {
  if (!val) return ''
  if (typeof val === 'string') return val.slice(0, 10)
  return val
}

export default function Attendance() {
  const [list, setList] = useState([])
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [form, setForm] = useState({ employee_id: '', date: '', status: 'Present' })
  const [saving, setSaving] = useState(false)
  const [selectedEmployeeId, setSelectedEmployeeId] = useState('')

  const fetchAttendance = async () => {
    setLoading(true)
    setError(null)
    try {
      let url = api.attendance
      if (selectedEmployeeId) url += `?employee_id=${encodeURIComponent(selectedEmployeeId)}`
      const data = await fetchApi(url)
      setList(Array.isArray(data) ? data : [])
    } catch (e) {
      setError(e.message || 'Failed to load attendance')
    } finally {
      setLoading(false)
    }
  }

  const fetchEmployees = async () => {
    try {
      const data = await fetchApi(api.employees)
      setEmployees(Array.isArray(data) ? data : [])
    } catch (_) {}
  }

  useEffect(() => { fetchEmployees() }, [])
  useEffect(() => { fetchAttendance() }, [selectedEmployeeId])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setSaving(true)
    setError(null)
    try {
      await fetchApi(api.attendance, {
        method: 'POST',
        body: JSON.stringify({
          employee_id: form.employee_id.trim(),
          date: form.date,
          status: form.status,
        }),
      })
      setForm({ employee_id: '', date: '', status: 'Present' })
      fetchAttendance()
    } catch (e) {
      setError(e.message)
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page">
      <h1>Attendance Management</h1>
      {error && <p className="error">{error}</p>}

      <section className="section">
        <h2>Mark attendance for an employee</h2>
        <form onSubmit={handleSubmit} className="form">
          <label>
            <span>Employee ID</span>
            <input
              required
              list="emp-list"
              placeholder="EMP001"
              value={form.employee_id}
              onChange={(e) => setForm((f) => ({ ...f, employee_id: e.target.value }))}
            />
          </label>
          <datalist id="emp-list">
            {employees.map((e) => (
              <option key={e.id} value={e.employee_id} />
            ))}
          </datalist>
          <label>
            <span>Date</span>
            <input
              required
              type="date"
              max={new Date().toISOString().slice(0, 10)}
              value={form.date}
              onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))}
            />
          </label>
          <label>
            <span>Status</span>
            <select
              value={form.status}
              onChange={(e) => setForm((f) => ({ ...f, status: e.target.value }))}
            >
              <option value="Present">Present</option>
              <option value="Absent">Absent</option>
            </select>
          </label>
          <button type="submit" disabled={saving}>{saving ? 'Saving…' : 'Mark Attendance'}</button>
        </form>
      </section>

      <section className="section">
        <h2>View attendance records for each employee</h2>
        <div className="filter">
          <label>
            <span>Employee</span>
            <select
              value={selectedEmployeeId}
              onChange={(e) => setSelectedEmployeeId(e.target.value)}
            >
              <option value="">All employees</option>
              {employees.map((e) => (
                <option key={e.id} value={e.employee_id}>{e.employee_id} {e.full_name}</option>
              ))}
            </select>
          </label>
        </div>
        {loading ? <p></p> : (
          <table className="table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Employee ID</th>
                <th>Name</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {list.length === 0 && (
                <tr><td colSpan={4}>No attendance records yet.</td></tr>
              )}
              {list.map((r) => (
                <tr key={r.id}>
                  <td>{formatDate(r.date)}</td>
                  <td>{r.employee_code || r.employee_id}</td>
                  <td>{r.employee_name }</td>
                  <td>{r.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  )
}
