import Header  from "./components/Header";
import Tasks from "./components/Tasks"
import './index.css'
import { useState } from 'react'
import AddTask from "./components/AddTask";

function App() {
    const [tasks , setTasks]= useState(
        [{
            id:1,
            taskname:"Learn Javascript",
            reminder:true,
            day:'July 20th',
        },
        {
            id:2,
            taskname:"Implement with React",
            reminder:true,
            day:'July 25th'
        },
        {
            id:3,
            taskname:"Fuck bitches",
            reminder:false,
            day:'Aug 1st'
    
        },
    ])

//add tasks
const addNew=(task) =>{
  console.log(task)
}

  //delete tasks

  const deleteTask=(id)=> {
    console.log('delete',tasks[id-1].taskname)
    setTasks(tasks.filter((task)=> task.id!==id))
  }
//goto url
  const gotoUrl=(id)=> {
    setTasks(
      tasks.map((task) => task.id==id ? {...task,reminder: !task.reminder}:task))
  }
     
  return (
    <div className="container">
      <Header />
      <AddTask />
      {tasks.length>0? <Tasks tasks={tasks} onDelete={deleteTask} onToggle={gotoUrl} />
      :'No Tasks!'
}
    </div>
  );
}




export default App;
