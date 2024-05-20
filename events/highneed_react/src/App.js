import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import NavBar from './components/NavBar';
import Home from './Pages/Home';
import Login from './Pages/Login';
import SearchEvent from './Pages/SearchEvent';
import Calendar from './Pages/Calendar';
import FBfanpage from './Pages/FBfanpage';


function App() {
  return (
    <>
    <Router>
      <NavBar />
      <Switch>
      <Route path='/' exact component={Home} />
      <Route path='/login' exact component={Login} />
      <Route path='/search-events' exact component={SearchEvent} />
      <Route path='/calendar' exact component={Calendar} />
      <Route path='/fanpage' exact component={FBfanpage} />
      </Switch>
    </Router>
    </>
  );
}

export default App;
