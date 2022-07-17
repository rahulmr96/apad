import { FaTimes } from 'react-icons/fa'

const Task =({task , onDelete, onToggle}) => {
    return (
    <div className={`task ${task.reminder? 'reminder': ''} `} >
        <h3>{task.taskname}<FaTimes style={{color:'red', Cursor:'pointer'}} onClick={()=> onDelete(task.id)}  /></h3>
    <div className='links' onDoubleClick={()=> onToggle(task.id)}>
        <p>{task.day}</p>
        </div>        
    </div>
    )
}

export default Task