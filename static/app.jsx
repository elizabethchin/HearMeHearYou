class App extends React.Component {
    render() {
        return <DateTime /> 
    }
}

class DateTime extends React.Component {
	constructor() {
		super()
		this.handleSubmit = this.handleSubmit.bind(this);
		this.handleInput = this.handleInput.bind(this);
	}

	handleSubmit(e) {
		e.preventDefault();
		console.log('firing')
		console.log(this.state.text)
		response = fetch('/submitForm')

	}

	handleInput(e) {
		this.setState({text: e.target.value})
	}

    render() {
        return(<div>
        		<p> date and time and stuff! </p>
        		<p> more stuff </p>
    			<input onChange={this.handleInput} type="text" name="name" value={this.state.text}/>
        		<button onChange={this.handleSubmit}> click me </button>
        	   </div>
        	)
    }
}

class submissionComplete



render <p> thank you for subbming, you have subbmited {this.props.number} previous claims





ReactDOM.render(
    <App />,
    document.getElementById("root")
);