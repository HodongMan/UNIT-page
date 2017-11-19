import React, { Component } from 'react';

import {Header, Navigation, MainContent, Footer} from './components';

export default class App extends Component {

    render() {
        return (
            <div>
                <Navigation />
                <Header />
                <MainContent />
                <Footer />
            </div>
        );
    }
}
