import React from 'react'
import { Link } from 'react-router-dom';
import './BottomBar.css';

function BottomBar() {
    return (
        <div className='bottom-bar'>
            <div className='contact-info'>
            <h2 center>Kontakt:</h2>
           
                <div className='contact-container'>
                    <div className='contact-icon'>
                        <svg width="22" height="18" viewBox="0 0 22 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2.19995" y="2.26282" width="17.6" height="13.5771" fill="white" />
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M0.011941 1.22869C0.011941 0.550109 0.559142 0 1.23416 0H20.7778C21.4528 0 22 0.550109 22 1.22869V15.1426C22 16.4998 20.9056 17.6 19.5556 17.6H2.44444C1.09441 17.6 0 16.4998 0 15.1426V1.62705C0 1.56854 0.0040699 1.51099 0.011941 1.45466V1.22869ZM2.44444 3.961V15.1426H19.5556V3.96142L13.5929 9.95559C12.161 11.3951 9.83938 11.3951 8.40748 9.95559L2.44444 3.961ZM4.36617 2.41763H17.6342L11.8645 8.21798C11.3872 8.69778 10.6133 8.69778 10.136 8.21798L4.36617 2.41763Z" fill="#FF0000" />
                        </svg>
                    </div>
                    <div className='contact-text'>
                        <p2>testowymail@mail.com</p2>
                    </div>
                </div>

                <Link className='contact' to={'/fanpage'}>
                    <div className='contact-container'>
                        <div className='contact-icon'>
                            <svg width="22" height="23" viewBox="0 0 22 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M22 11.3492C22 5.08071 17.0756 0 11 0C4.92438 0 0 5.08071 0 11.3492C0 17.0145 4.02027 21.7096 9.28219 22.5616V14.6327H6.49151V11.3492H9.28219V8.84927C9.28219 6.00731 10.9216 4.43396 13.4351 4.43396C14.6405 4.43396 15.9003 4.65784 15.9003 4.65784V7.45005H14.514C13.1458 7.45005 12.7238 8.3269 12.7238 9.2224V11.3492H15.7737L15.2855 14.6327H12.7238V22.5616C17.9797 21.7096 22 17.0145 22 11.3492Z" fill="#1877F2" />
                                <path d="M15.2794 14.6327L15.7677 11.3492H12.7178V9.22239C12.7178 8.32689 13.1457 7.45005 14.5079 7.45005H15.8942V4.65783C15.8942 4.65783 14.6345 4.43396 13.429 4.43396C10.9156 4.43396 9.27616 6.0073 9.27616 8.84927V11.3492H6.48547V14.6327H9.27616V22.5616C9.83671 22.6549 10.4093 22.6984 10.994 22.6984C11.5786 22.6984 12.1512 22.6487 12.7118 22.5616V14.6327H15.2794Z" fill="white" />
                            </svg>
                        </div>
                        <div className='contact-text'>
                            <p2>Facebook fanpage</p2>
                        </div>
                    </div>
                </Link>

             </div>
        </div>
        )
}
export default BottomBar;