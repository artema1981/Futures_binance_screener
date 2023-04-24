import './App.css';
import React from 'react';
import axios from 'axios';

class DepthBookList extends React.Component{
    state = {details: [], }

    componentDidMount() {
        let  data;
        axios.get('http://127.0.0.1:8000/')
        .then(res => {
          data = res.data;
          this.setState({
                details: data
          });
        })
          .catch(err => {
                console.log(err);
            })
    }
    render() {
        return (
            <div >
                <hr></hr>
                {this.state.details.map((output, id) => (
                    <div key={id} className='item'>
                        <div className='item_symbol'>
                            <h5>{output.get_unit_data.symbol}</h5>

                        </div>
                        <div>
                            <p className='s'>{output.get_unit_data.spot.best_ask}</p>
                            <hr></hr>
                            <p className='f'>{output.get_unit_data.spot.best_bid}</p>
                        </div>
                        <div>
                            <p className='s'>{output.get_unit_data.spot.percent_ask}</p>
                            <hr></hr>
                            <p className='f'>{output.get_unit_data.spot.percent_bid}</p>
                        </div>
                        <div>
                            <p className='s'>{output.get_unit_data.spot.ask_volume_usdt}</p>
                            <hr></hr>
                            <p className='f'>{output.get_unit_data.spot.bid_volume_usdt}</p>
                        </div>
                    </div>
                    ))}
            </div>
        )
    }
}


export default DepthBookList;