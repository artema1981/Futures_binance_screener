import './App.css';
import React from "react";
import './syles/App.css'
import DepthBookList from "./DepthBookList";
function App() {

    function K100() {

    }
    function K500() {

    }

    function K750() {

    }
    function M1() {

    }
    return (
        <div className="App">
            <div className='button'>
                <button onClick={K100}>100K</button>
                <button onClick={K500}>500K</button>
                <button onClick={K750}>750K</button>
                <button onClick={M1}>1M</button>
            </div>
            <div>
            <DepthBookList/>
            </div>
        </div>
    )
}
export default App;



