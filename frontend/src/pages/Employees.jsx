import { useState, useEffect } from 'react'
import { api, fetchApi } from '../api'

export default function Employees() {
  const [list, setList] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [form, setForm] = useState({ employee_id: '', full_name: '', email: '', department: '' })
  const [saving, setSaving] = useState(false)
  const [deleteConfirm, setDeleteConfirm] = useState(null)

  const fetchEmployees = async () => {
    setLoading(true)
    setError(null)
    try {
      const data = await fetchApi(api.employees)
      setList(Array.isArray(data) ? data : [])
    } catch (e) {
      setError(e.message || 'Failed to load employees')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { fetchEmployees() }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setSaving(true)
    setError(null)
    try {
      await fetchApi(api.employees, {
        method: 'POST',
        body: JSON.stringify(form),
      })
      setForm({ employee_id: '', full_name: '', email: '', department: '' })
      fetchEmployees()
    } catch (e) {
      setError(e.message)
    } finally {
      setSaving(false)
    }
  }

  const handleDeleteClick = (emp) => {
    setDeleteConfirm({ id: emp.id, name: emp.full_name || emp.employee_id })
  }

  const handleDeleteConfirm = async () => {
    if (!deleteConfirm) return
    setError(null)
    try {
      await fetchApi(api.employees + deleteConfirm.id, { method: 'DELETE' })
      setDeleteConfirm(null)
      fetchEmployees()
    } catch (e) {
      setError(e.message)
    }
  }

  return (
    <div className="page">
      <h1>Employee Management</h1>
      {error && <p className="error">{error}</p>}

      {deleteConfirm && (
        <div className="confirm-box">
          <p><strong>Delete this employee?</strong></p>
          <p>{deleteConfirm.name}</p>
          <div className="confirm-actions">
            <button type="button" onClick={() => setDeleteConfirm(null)}>Cancel</button>
            <button type="button" className="btn-danger" onClick={handleDeleteConfirm}>Delete</button>
          </div>
        </div>
      )}

      <section className="section">
        <h2>Add a new employee</h2>
        <form onSubmit={handleSubmit} className="form">
          <label>
            <span>Employee ID</span>
            <input
              required
              placeholder="EMP001"
              value={form.employee_id}
              onChange={(e) => setForm((f) => ({ ...f, employee_id: e.target.value.trim() }))}
            />
          </label>
          <label>
            <span>Full Name</span>
            <input
              required
              placeholder="Full Name"
              value={form.full_name}
              onChange={(e) => setForm((f) => ({ ...f, full_name: e.target.value }))}
            />
          </label>
          <label>
            <span>Email Address</span>
            <input
              required
              type="email"
              placeholder="email@example.com"
              value={form.email}
              onChange={(e) => setForm((f) => ({ ...f, email: e.target.value }))}
            />
          </label>
          <label>
            <span>Department</span>
            <input
              placeholder="Optional"
              value={form.department}
              onChange={(e) => setForm((f) => ({ ...f, department: e.target.value }))}
            />
          </label>
          <button type="submit" disabled={saving}>{saving ? 'Adding…' : 'Add Employee'}</button>
        </form>
      </section>

      <section className="section">
        <h2>View all employees</h2>
        {loading ? <p></p> : (
          <table className="table">
            <thead>
              <tr>
                <th>Employee ID</th>
                <th>Full Name</th>
                <th>Email Address</th>
                <th>Department</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {list.length === 0 && (
                <tr><td colSpan={5}>No employees yet.</td></tr>
              )}
              {list.map((emp) => (
                <tr key={emp.id}>
                  <td>{emp.employee_id}</td>
                  <td>{emp.full_name}</td>
                  <td>{emp.email}</td>
                  <td>{emp.department || '–'}</td>
                  <td>
                    <button type="button" className="btn-danger" onClick={() => handleDeleteClick(emp)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  )
}
