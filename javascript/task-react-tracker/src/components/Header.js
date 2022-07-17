import React from 'react'
import PropTypes from 'prop-types'
import Button from './Button'


const Header = ({title}) => {
    const onClick =()=>{
        console.log('click')
    }
  
    return (
    <header className='header'>
        <h1>{title}
        <Button color='blue' text='Add' onClick={onClick} />
         </h1>
         
    </header>
  )
}

Header.defaultProps={
    title:'Task Tracker',
}

export default Header