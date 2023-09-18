import logo from './logo.svg';
import './App.css';
import Test from './Test.js'

function App() {
  return (
    <div>
      App Component
      <Test myParam="First animal" animal="dog"/>
      <Test myParam="Second animal" animal="cat"/>
    </div>
  );
}

export default App;
