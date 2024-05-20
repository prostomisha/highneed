import React from 'react';
import { Link } from 'react-router-dom';
import { ResponsiveImage, ResponsiveImageSize } from 'react-responsive-image';
import './Home.css'
import './Home-responsive.css'
import BottomBar from '../components/BottomBar';

const small = '/images/img-article-s.jpg';
const medium = '/images/img-article-m.jpg';
const large = '/images/img-article.jpg';

const small_2 = '/images/img-article2-s.jpg';
const medium_2 = '/images/img-article2-m.jpg';
const large_2 = '/images/img-article2.jpg';

const small_3 = '/images/img-map-s.png';
const medium_3 = '/images/img-map-m.png';
const large_3 = '/images/img-map.png';


function Home() {
    return (
        <>
            <div className='homepage'>
                <div className='sport-list'>

                    <button className='button categories'>
                        <div className='categories'>
                            Sport
                        </div>
                    </button>
                    <button className='button categories'>
                        <div className='categories'>
                            Plastyka
                        </div>
                    </button>
                    <button className='button categories'>
                        <div className='categories'>
                            Muzyka
                        </div>
                    </button>
                    <button className='button categories'>
                        <div className='text'>
                            Taniec
                        </div>
                    </button>
                    <button className='button categories'>
                        <div className='search-text'>
                            Edukacja
                        </div>
                    </button>


                </div>

                <div className='article-container'>
                    <div className='article-img'>
                        <ResponsiveImage>
                            <ResponsiveImageSize
                                minWidth={0}
                                path={small}

                            />
                            <ResponsiveImageSize
                                minWidth={416}
                                path={medium}
                            />
                            <ResponsiveImageSize
                                minWidth={801}
                                path={large}
                            />
                        </ResponsiveImage>
                    </div>

                    <div className='article-text'>
                        <h1>Witamy na stronie HighNeed </h1>
                        <p>HighNeed.pl jest portalem do planowania aktywności dla rodzin z dziećmi w Poznaniu.</p>
                    </div>



                </div>
                <div class='line'></div>

                <div className='article2-container'>
                    <div className='article2-text'>
                        <h1>Wyszukiwanie wydarzeń w Twojej okolicy</h1>
                        <p>Znajdź grupy i wydarzenia na terenie Poznania, dzięki którym Twoje dziecko rozwinie swoje zainteresowania oraz zawrze nowe znajomości. </p>

                        <Link className='center searching' to={'/search-events'}>
                            <button className='button'>
                                <div className='search-components'>
                                    <div className='search button-icon'>
                                        <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M16.9325 15.7562C18.969 13.1408 18.785 9.35694 16.3807 6.95262C13.7772 4.34913 9.55612 4.34913 6.95262 6.95262C4.34913 9.55612 4.34913 13.7772 6.95262 16.3807C9.35694 18.785 13.1408 18.969 15.7562 16.9325C15.7675 16.9453 15.7793 16.9578 15.7915 16.97L19.327 20.5055C19.6524 20.8309 20.1801 20.8309 20.5055 20.5055C20.8309 20.1801 20.8309 19.6524 20.5055 19.327L16.97 15.7915C16.9578 15.7793 16.9453 15.7675 16.9325 15.7562ZM15.2022 8.13113C17.1548 10.0838 17.1548 13.2496 15.2022 15.2022C13.2496 17.1548 10.0838 17.1548 8.13113 15.2022C6.17851 13.2496 6.17851 10.0838 8.13113 8.13113C10.0838 6.17851 13.2496 6.17851 15.2022 8.13113Z" fill="white" />
                                        </svg>
                                    </div>
                                    <div className='search-text'>
                                        Wyszukaj wydarzenia
                                </div>
                                </div>
                            </button>
                        </Link>
                    </div>

                    <div className='article-img2'>
                        <ResponsiveImage>
                            <ResponsiveImageSize
                                minWidth={0}
                                path={small_2}
                            />
                            <ResponsiveImageSize
                                minWidth={416}
                                path={medium_2}
                            />
                            <ResponsiveImageSize
                                minWidth={801}
                                path={large_2}
                            />
                        </ResponsiveImage>
                    </div>
                </div>
                <div class='line'></div>

                <div className='article3-container'>
                    <div className='article-img3'>
                        <ResponsiveImage>
                            <ResponsiveImageSize
                                minWidth={0}
                                path={small_3}
                            />
                            <ResponsiveImageSize
                                minWidth={416}
                                path={medium_3}
                            />
                            <ResponsiveImageSize
                                minWidth={801}
                                path={large_3}
                            />
                        </ResponsiveImage>
                    </div>
                </div>
                <div class='line'></div>

                <div className='article4-container'>
                    <div className='article4-text'>
                        <h1>Nadchodzące wydarzenia</h1>

                        <p>* Będzie po połączeniu zaimportowanych wydarzeń *</p> 
                    </div>
                </div>
                <div class='line'></div>

                <BottomBar />
            </div>
        </>
    );
}

export default Home;