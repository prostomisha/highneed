import React from 'react';
import './Events.css';
import EventItem from './EventItem';

function Events() {
  return (
    <div className='events'>
      <div className='events__container'>
          <ul className='events__items'>
            <EventItem
              src='images/img-1.jpg'
              data='29.07.2020 Piątek, 18:00 - 20:00'
              title='Współne zabawy na placu zabaw'
              category='Zabawa'
              age = '5-7 lat'
              address = 'Hetmańska 48, Poznań'
              path='/'
            />
            <EventItem
              src='images/img-2.jpg'
              data='29.07.2020 Piątek, 18:00 - 20:00'
              title='Współne zabawy na placu zabaw'
              category='Zabawa'
              age = '5-7 lat'
              address = 'Hetmańska 48, Poznań'
              path='/'
            />
          </ul>
      </div>
    </div>
  );
}

export default Events;
