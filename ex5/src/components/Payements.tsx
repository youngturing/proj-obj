import React from 'react';
import axios from 'axios';

const Payements: React.FC = () => {

    const sendPayementData = async () => {
        try {
            await axios.post('http://localhost:3001/api/payments', {data: 'Payements data'});
            console.log('Payements data have been sent.');
        } catch(error) {
            console.log(error);
        }
    };

    return (
        <div>
            <h2>Payements</h2>
            <button onClick={sendPayementData}>
                Send payements data
            </button>
        </div>
    );
};

export default Payements;
