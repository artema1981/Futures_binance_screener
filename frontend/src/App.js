import './App.css';
import React, { useEffect, useState } from "react";
import './syles/App.css'
import DepthBookList from "./DepthBookList";

function K100(setUSDTVolume) {
  fetch('http://127.0.0.1:8000?USDT_volume=1000000')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      setUSDTVolume(1000000);
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
}

function K500() {
  // add code to send GET request to server for 500K
}

function K750() {
  // add code to send GET request to server for 750K
}

function M1() {
  // add code to send GET request to server for 1M
}

function App() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [usdtVolume, setUSDTVolume] = useState(null);

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleScroll = () => {
    const scrollTop = window.pageYOffset;
    if (scrollTop > 0) {
      setIsScrolled(true);
    } else {
      setIsScrolled(false);
    }
  }

  return (
    <div className="App">
      <header style={{ position: isScrolled ? 'fixed' : 'static', top: 0 }}>
        <nav>
          <ul>
            <div className='button'>
              <button className='button' onClick={() => K100(setUSDTVolume)}>250K</button>
              <button className='button' onClick={K500}>500K</button>
              <button className='button' onClick={K750}>750K</button>
              <button className='button' onClick={M1}>1M</button>
            </div>
            <div>
              <tr>
                <th className='row_head' scope="row"><p>SYMBOL</p></th>
                <th className='row_head' scope="row"><p>price</p></th>
                <th className='row_head' scope="row"><p>%</p></th>
                <th className='row_head' scope="row"><p>USDT</p></th>
                <th className='row_head' scope="row"><p>price</p></th>
                <th className='row_head' scope="row"><p>%</p></th>
                <th className='row_head' scope="row"><p>USDT</p></th>
              </tr>
            </div>
          </ul>
        </nav>
      </header>
      <div>
        <DepthBookList/>
      </div>
    </div>
  );
}

export default App;



