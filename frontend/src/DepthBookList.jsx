import './App.css';
import React from 'react';
import axios from 'axios';
import Header from "./Header";

class DepthBookList extends React.Component {
    state = {details: [],}

    componentDidMount() {
        let data;
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

    M1 = () => {
        axios
            .get('http://127.0.0.1:8000/', {
                params: {
                    USDT_volume: 1000000,
                },
            })
            .then((res) => {
                this.setState({
                    details: res.data,
                });

            })
            .catch((err) => {
                console.log(err);
            });
    };
    K750 = () => {
        axios
            .get('http://127.0.0.1:8000/', {
                params: {
                    USDT_volume: 750000,
                },
            })
            .then((res) => {
                this.setState({
                    details: res.data,
                });

            })
            .catch((err) => {
                console.log(err);
            });
    };
    K500 = () => {
        axios
            .get('http://127.0.0.1:8000/', {
                params: {
                    USDT_volume: 750000,
                },
            })
            .then((res) => {
                this.setState({
                    details: res.data,
                });

            })
            .catch((err) => {
                console.log(err);
            });
    };
    K500 = () => {
        axios
            .get('http://127.0.0.1:8000/', {
                params: {
                    USDT_volume: 500000,
                },
            })
            .then((res) => {
                this.setState({
                    details: res.data,
                });

            })
            .catch((err) => {
                console.log(err);
            });
    };
    K250 = () => {
        axios
            .get('http://127.0.0.1:8000/', {
                params: {
                    USDT_volume: 250000,
                },
            })
            .then((res) => {
                this.setState({
                    details: res.data,
                });

            })
            .catch((err) => {
                console.log(err);
            });
    };

    render() {
        return (
            <div>
                <div className='button'>
                    <button className='button' onClick={this.K250}>250K</button>
                    <button className='button' onClick={this.K500}>500K</button>
                    <button className='button' onClick={this.K750}>750K</button>
                    <button className='button' onClick={this.M1}>1M</button>
                </div>
                <div>
                    <Header/>
                </div>
                {/*<button onClick={this.M1}>Обновить данные</button>*/}
                <hr></hr>
                {this.state.details.map((output, id) => {
                    console.log(output)
                    if (output.get_unit_data) {
                        return (
                            <div key={id} className='item'>
                                <div>
                                    <tbody>
                                    <tr>
                                        <th className='item_symbol'><p>{output.get_unit_data.symbol}</p></th>
                                        <tr>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.spot.best_ask}</p></th>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.spot.percent_ask}</p></th>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.spot.ask_volume_usdt}</p></th>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.future.best_ask}</p></th>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.future.percent_ask}</p></th>
                                            <th className='row_ask' scope="row">
                                                <p>{output.get_unit_data.future.ask_volume_usdt}<a>.</a></p></th>
                                        </tr>
                                        <tr className="table-primary">
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.spot.best_bid}</p></th>
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.spot.percent_bid}</p></th>
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.spot.bid_volume_usdt}</p></th>
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.future.best_bid}</p></th>
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.future.percent_bid}</p></th>
                                            <th className='row_bid' scope="row">
                                                <p>{output.get_unit_data.future.bid_volume_usdt}<a>.</a></p></th>
                                        </tr>
                                    </tr>
                                    </tbody>
                                </div>

                            </div>
                        );
                    } else {
                        return null;
                    }
                })}
            </div>
        );
    }
}


export default DepthBookList;
