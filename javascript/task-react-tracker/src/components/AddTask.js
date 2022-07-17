import { useState } from 'react' 

const AddTask=({onAdd}) => {
    const [taskname,setText]=useState('')
    const [day,setDay]=useState('')
    const [reminder,setReminder]=useState(false)
    
    const onSubmit=(e)=>{
        e.preventDefault()
        onAdd({taskname,day,reminder})

        setText('')
        setDay('')
        setReminder(false)
    }


    return(
        <form className="add-form" onSubmit={onSubmit}>
        <div className="form-control">
            <label>Task </label>
            <input type='text' placeholder="Add Task" value={taskname} 
                onChange={(e) => setText(e.target.value)}>
            </input>
            </div>
        <div className="form-control">
            <label>Day </label>
            <input type='text' placeholder="Which Day?" value={day} 
                onChange={(e) => setDay(e.target.value)}>
            </input>
            </div>
        <div className="form-control-check">
            <label>Reminder</label>
            <input type='checkbox' 
            checked={reminder}
            placeholder="Reminder?" value={reminder} 
                onChange={(e) => setReminder(e.currentTarget.checked)}>
            </input>
            </div>
        <input type='submit' value='Save Task' className="btn btn-block"></input>
        </form>
    )
}

export default AddTask