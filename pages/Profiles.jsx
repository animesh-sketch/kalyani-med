import { useState } from 'react'
import { initialProfiles } from '../data/profiles'

function Profiles({ profiles = initialProfiles, onViewProfile }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [filterProfession, setFilterProfession] = useState('')
  const [filterAge, setFilterAge] = useState('')
  const [filterLocation, setFilterLocation] = useState('')

  const filteredProfiles = profiles.filter(profile => {
    const matchesSearch = profile.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          profile.location.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesProfession = !filterProfession || profile.profession.includes(filterProfession)
    const matchesAge = !filterAge || 
      (filterAge === '18-25' && profile.age <= 25) ||
      (filterAge === '26-30' && profile.age > 25 && profile.age <= 30) ||
      (filterAge === '30+' && profile.age > 30)
    const matchesLocation = !filterLocation || profile.location === filterLocation
    return matchesSearch && matchesProfession && matchesAge && matchesLocation
  })

  const locations = [...new Set(profiles.map(p => p.location))]
  const professions = [...new Set(profiles.map(p => p.profession))]

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="text-center mb-10">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Browse Profiles</h1>
        <p className="text-gray-600">Find your perfect match from our verified profiles</p>
      </div>
      
      <div className="bg-white rounded-xl shadow-md p-6 mb-8">
        <div className="grid md:grid-cols-4 gap-4">
          <div className="relative">
            <input
              type="text"
              placeholder="Search by name..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
            />
          </div>
          <select
            value={filterAge}
            onChange={(e) => setFilterAge(e.target.value)}
            className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
          >
            <option value="">All Ages</option>
            <option value="18-25">18-25 years</option>
            <option value="26-30">26-30 years</option>
            <option value="30+">30+ years</option>
          </select>
          <select
            value={filterLocation}
            onChange={(e) => setFilterLocation(e.target.value)}
            className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
          >
            <option value="">All Locations</option>
            {locations.map(loc => <option key={loc} value={loc}>{loc}</option>)}
          </select>
          <select
            value={filterProfession}
            onChange={(e) => setFilterProfession(e.target.value)}
            className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
          >
            <option value="">All Professions</option>
            {professions.map(prof => <option key={prof} value={prof}>{prof}</option>)}
          </select>
        </div>
      </div>

      <div className="flex justify-between items-center mb-6">
        <p className="text-gray-600">{filteredProfiles.length} profiles found</p>
        <select className="px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500">
          <option>Sort by: Latest</option>
          <option>Sort by: Age</option>
        </select>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {filteredProfiles.map(profile => (
          <div 
            key={profile.id} 
            className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-2xl transition-all duration-300 cursor-pointer transform hover:-translate-y-1"
            onClick={() => onViewProfile(profile)}
          >
            <div className="relative bg-gradient-to-br from-rose-100 to-pink-100 h-40 flex items-center justify-center text-7xl">
              {profile.image}
              {profile.verified && (
                <span className="absolute top-3 right-3 bg-green-500 text-white text-xs px-2 py-1 rounded-full flex items-center gap-1">
                  ✓ Verified
                </span>
              )}
            </div>
            <div className="p-5">
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-lg font-bold text-gray-800">{profile.name}</h3>
                <span className="text-rose-600 font-semibold">{profile.age} yrs</span>
              </div>
              <p className="text-gray-500 text-sm mb-1">{profile.profession}</p>
              <div className="flex items-center gap-2 text-gray-500 text-sm mb-1">
                <span>📍</span> {profile.location}
              </div>
              <div className="flex items-center gap-2 text-gray-500 text-sm mb-3">
                <span>🎓</span> {profile.education}
              </div>
              <button className="w-full bg-gradient-to-r from-rose-500 to-pink-500 text-white py-2.5 rounded-lg hover:from-rose-600 hover:to-pink-600 transition font-medium">
                View Profile
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredProfiles.length === 0 && (
        <div className="text-center py-16">
          <div className="text-6xl mb-4">😔</div>
          <p className="text-gray-500 text-lg">No profiles found matching your criteria.</p>
          <button 
            onClick={() => {setSearchTerm(''); setFilterProfession(''); setFilterAge(''); setFilterLocation('')}}
            className="mt-4 text-rose-600 hover:underline"
          >
            Clear filters
          </button>
        </div>
      )}
    </div>
  )
}

export default Profiles
