import React from 'react';
import { Link } from 'react-router-dom';


function EventItem(props) {
  return (
    <>
      <li className='events__item'>
        <Link className='events__item__img__link' to={props.path}>
            <img
              className='events__item__img'
              alt='Event Image'
              width='200px'
              height='200px'
              src={props.src}
              />

        </Link>
          <div className='events__item__info'>
          <h5 className='events__item__data'>{props.data}</h5>

          <Link className='events__item__link' to={props.path}>
                <h4 className='events__item__title'>{props.title}</h4>
          </Link> 
            <h5 className='events__item__category'>{props.category}</h5>
            <h5 className='events__item__age'>{props.age}</h5>
            <h5 className='events__item__address'>{props.address}</h5>

          <Link className='events__item__link' to={props.path}>
                <button className='button button-details'>Szczegóły</button>  
           </Link>
           <Link className='events__item__link' to={props.path}>
                <button className='button button-add'>Dodaj do listy</button>
           </Link>
          </div>
      </li>
    </>
  );
}

export default EventItem;
