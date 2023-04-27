import React, {useEffect, useState} from 'react';

const Header = () => {
    const [isScrolled, setIsScrolled] = useState(false);
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
        <div>
            <header style={{position: isScrolled ? 'fixed' : 'static', top: 0}}>
                <nav>
                    <ul>
                        <div className='button'>

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
        </div>
    );
};

export default Header;