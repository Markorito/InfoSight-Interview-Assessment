import logo from './logo.svg';
import './App.css';
import React from 'react'
import { useEffect, useState } from "react"
import Axios from 'axios'

<title>ID PASSPORT CLASSIFIER</title>

function App ( ) {

  const [data, setData] = useState(null)
  const [selectedFile, setSelectedFile] = useState(null);
  const [isFilePicked, setIsFilePicked] = useState(false);

  const changeHandler = (event) => {
      setSelectedFile(event.target.files[0]);
      setIsFilePicked(true);
  };
  
  const handleSubmit = event => {
    event.preventDefault();
    const formData2 = new FormData();
    formData2.append(
      "file",
      selectedFile,
      selectedFile.name
    );
    const requestOptions = {
      method: 'POST',
      //headers: { 'Content-Type': 'multipart/form-data' }, // DO NOT INCLUDE HEADERS
      body: formData2
  };
    fetch('http://127.0.0.1:8000/predict', requestOptions)
      .then(response => response.json())
      .then(function (response) {
        console.log('response')
        setData(response)
          });		  
}

 //useEffect(() => { fetch('http://127.0.0.1:8000') .then(res => { return res.json(); }) .then(data => { setData(data); }) }, [])

  return (  <div style={{ justifyContent:'center', alignItems:'center', height: '100vh'}}>
	  <h1>ID PASSPORT CLASSIFIER</h1>
      <form onSubmit={handleSubmit}>
        <fieldset>
            <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg"/>
        </fieldset>
        <button type="submit">Save</button>
      </form>
	  <div>
	  <p> {JSON.stringify(data)} </p>
	  </div>
  </div>
);
}


export default App