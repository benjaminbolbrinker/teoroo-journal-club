use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod fib;

#[pyfunction]
fn fib(a: u64) -> PyResult<u64> {
    Ok(fib::fib(a))
}

#[pymodule]
fn fib_rs(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)?;

    Ok(())
}