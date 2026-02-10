import { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import { checkBackendConnection, api, fetchApi } from './api'
import Employees from './pages/Employees'
import Attendance from './pages/Attendance'
import './App.css'

function App() {
  const [apiStatus, setApiStatus] = useState(null) // null = checking, true = connected, false = disconnected

  useEffect(() => {
    let cancelled = false
    async function check() {
      const result = await checkBackendConnection()
      if (!cancelled) setApiStatus(result.ok)
    }
    check()
    return () => { cancelled = true }
  }, [])

  return (
    <div className="app">
      <nav className="nav">
        <Link to="/">Home</Link>
        <Link to="/employees">Employees</Link>
        <Link to="/attendance">Attendance</Link>
      </nav>
      <main className="main">
        <Routes>
          <Route path="/" element={<Home apiConnected={apiStatus} />} />
          <Route path="/employees" element={<Employees />} />
          <Route path="/attendance" element={<Attendance />} />
        </Routes>
      </main>
    </div>
  )
}

function Home({ apiConnected }) {
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (apiConnected === false) {
      setLoading(false)
      return
    }
    let cancelled = false
    async function fetchList() {
      setLoading(true)
      setError(null)
      try {
        const data = await fetchApi(api.employees)
        if (!cancelled) setEmployees(Array.isArray(data) ? data : [])
      } catch (e) {
        if (!cancelled) setError(e.message)
      } finally {
        if (!cancelled) setLoading(false)
      }
    }
    fetchList()
    return () => { cancelled = true }
  }, [apiConnected])

  return (
    <div>
      <h1>Assessment</h1>
      <p>Employee & Attendance Management</p>
      {apiConnected === false && (
        <p className="error"></p>
      )}
      <h2>All Employees</h2>
      {loading && <p></p>}
      {error && <p className="error">{error}</p>}
      {!loading && !error && (
        <table className="table">
          <thead>
            <tr>
              <th>Employee ID</th>
              <th>Full Name</th>
              <th>Email</th>
              <th>Department</th>
            </tr>
          </thead>
          <tbody>
            {employees.length === 0 && (
              <tr><td colSpan={4}>No employees yet.</td></tr>
            )}
            {employees.map((emp) => (
              <tr key={emp.id}>
                <td>{emp.employee_id}</td>
                <td>{emp.full_name}</td>
                <td>{emp.email}</td>
                <td>{emp.department}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

export default App
