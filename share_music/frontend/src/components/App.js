import React , {Component} from 'react'
import renderer, { render } from 'react-dom'

export default class App extends Component{
    constructor(props){
        super(props)
    }
    render(){
        return (
        <h1>   React + Django Works ! </h1>
        )
    }
}
const appDiv = document.getElementById("app")

render(<App/> , appDiv)