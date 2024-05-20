import React from 'react'
import './Login.css'

function Login() {
    return (
        <div className='signup' >

            <div className='login-container'>
                <div class='line'></div>
                <form>
                    <h3>Logowanie</h3>
                    <div className='input-container'>
                        <p>E-mail:</p>
                        <input type='tekst' />
                   
                        <p>Has�o:</p>
                        <input type='tekst' />

                        <button className='button login'>
                                Zaloguj sie
                         </button>
                    </div>

                    <div className='login-bottom'>
                        <div className='text-button'>
                            <p>Pierwszy raz na stronie?</p>

                            <button className='button register'>
                                Zarejestruj si�
                             </button>
                        </div>
                        <div className='text-button'>
                            <p>Nie pami�tasz has�a?</p>
                            <button className='button reset'>
                                Zresetuj has�o
                            </button>
                        </div>
                    </div>

                </form>
                <div class='line'></div>
            </div>
        </div>
    );
}
export default Login;