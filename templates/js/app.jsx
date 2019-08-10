import DateTime from './dateTime';

class App extends React.Component {
    render() {
        return( <DateTime> )
    }
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
);

class Todays_date extends React.Component {
    render() {
        return<p> Today's Date: {this.props.Todays_date}</p>
    }
}

ReactDOM.render(
    <Todays_date />,
    document.getElementById("root")
);