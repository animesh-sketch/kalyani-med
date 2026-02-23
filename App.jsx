import { useState } from 'react'
import Home from './pages/Home'
import Profiles from './pages/Profiles'
import ProfileDetail from './pages/ProfileDetail'
import CreateProfile from './pages/CreateProfile'
import { initialProfiles } from './data/profiles'

function App() {
  const [currentPage, setCurrentPage] = useState('home')
  const [selectedProfile, setSelectedProfile] = useState(null)
  const [profiles, setProfiles] = useState(initialProfiles)

  const renderPage = () => {
    switch (currentPage) {
      case 'profiles':
        return <Profiles profiles={profiles} onViewProfile={handleViewProfile} />
      case 'profileDetail':
        return <ProfileDetail profile={selectedProfile} onBack={() => setCurrentPage('profiles')} />
      case 'createProfile':
        return <CreateProfile onSubmit={handleCreateProfile} onCancel={() => setCurrentPage('home')} />
      default:
        return <Home onNavigate={setCurrentPage} />
    }
  }

  const handleViewProfile = (profile) => {
    setSelectedProfile(profile)
    setCurrentPage('profileDetail')
  }

  const handleCreateProfile = (newProfile) => {
    const profileWithId = { ...newProfile, id: Date.now(), verified: false }
    setProfiles([profileWithId, ...profiles])
    setCurrentPage('profiles')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-rose-50 via-white to-pink-50">
      <nav className="bg-white/80 backdrop-blur-md shadow-lg sticky top-0 z-50 border-b border-rose-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div 
              className="flex items-center cursor-pointer group" 
              onClick={() => setCurrentPage('home')}
            >
              <span className="text-3xl group-hover:scale-110 transition">💍</span>
              <span className="ml-2 text-xl font-bold bg-gradient-to-r from-rose-500 to-pink-500 bg-clip-text text-transparent">
                ShaadiZone
              </span>
            </div>
            <div className="flex items-center gap-6">
              <button 
                onClick={() => setCurrentPage('home')}
                className={`text-sm font-medium transition ${currentPage === 'home' ? 'text-rose-600' : 'text-gray-600 hover:text-rose-600'}`}
              >
                Home
              </button>
              <button 
                onClick={() => setCurrentPage('profiles')}
                className={`text-sm font-medium transition ${currentPage === 'profiles' ? 'text-rose-600' : 'text-gray-600 hover:text-rose-600'}`}
              >
                Browse Profiles
              </button>
              <button 
                onClick={() => setCurrentPage('createProfile')}
                className="bg-gradient-to-r from-rose-500 to-pink-500 text-white px-5 py-2 rounded-full text-sm font-medium hover:shadow-lg hover:scale-105 transition"
              >
                Create Profile
              </button>
            </div>
          </div>
        </div>
      </nav>
      {renderPage()}
      <footer className="bg-gray-900 text-white py-12 mt-16">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <span className="text-2xl">💍</span>
                <span className="text-xl font-bold text-rose-400">ShaadiZone</span>
              </div>
              <p className="text-gray-400 text-sm">Find your perfect partner and start your happily ever after.</p>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Quick Links</h4>
              <ul className="space-y-2 text-gray-400 text-sm">
                <li className="hover:text-rose-400 cursor-pointer">About Us</li>
                <li className="hover:text-rose-400 cursor-pointer">Success Stories</li>
                <li className="hover:text-rose-400 cursor-pointer">Contact Us</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Legal</h4>
              <ul className="space-y-2 text-gray-400 text-sm">
                <li className="hover:text-rose-400 cursor-pointer">Privacy Policy</li>
                <li className="hover:text-rose-400 cursor-pointer">Terms of Service</li>
                <li className="hover:text-rose-400 cursor-pointer">Refund Policy</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Connect With Us</h4>
              <div className="flex gap-4">
                <span className="text-2xl cursor-pointer hover:scale-110 transition">📘</span>
                <span className="text-2xl cursor-pointer hover:scale-110 transition">📸</span>
                <span className="text-2xl cursor-pointer hover:scale-110 transition">🐦</span>
              </div>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400 text-sm">
            <p className="mb-2">Founded by <span className="text-rose-400 font-semibold">Animesh</span></p>
            © 2026 ShaadiZone. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App
