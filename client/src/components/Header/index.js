import React, {PureComponent} from 'react';


export default class Header extends PureComponent{

    render(){
        return(
            <div className="intro-header">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12">
                            <div className="intro-message">
                                <h1></h1>
                                <h3></h3>
                                <hr className="intro-divider" />
                                <ul className="list-inline intro-social-buttons">

                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}


/*

ul tag 안에 있는 아이콘들 생성 할때
<li>
    <a href="https://www.facebook.com/unithonWithU/" className="btn btn-default btn-lg"><i className="fa fa-facebook fa-fw"></i> <span className="network-name">Facebook</span></a>
</li>
<li>
    <a href="https://www.facebook.com/unithonWithU/" className="btn btn-default btn-lg"><i className="fa fa-github fa-fw"></i> <span className="network-name">Github</span></a>
</li>

*/
