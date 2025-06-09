<template>
  <div class="profiles">
    <div v-for="profile in profiles" :key="profile.id" class="profile-card">
      <img :src="`/profiles/face_${profile.id}.png`" :alt="profile.name" class="profile-img" />
      <div class="profile-name">{{ `${profile.id}. ${profile.name}` }}</div>
      <div class="profile-detail">Name (cont): {{ profile.name_cont }}</div>
      <div class="profile-detail">K/C: {{ profile.kc }}</div>
      <div class="profile-detail">Birthday: {{ profile.birthday }}</div>
      <div class="profile-detail">Country: {{ profile.country }}</div>
      <div class="profile-detail">Company: {{ profile.company }}</div>
      <div class="profile-detail">Notes: {{ profile.notes }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Replace with your published CSV URL
const SHEET_CSV_URL = 'https://docs.google.com/spreadsheets/d/1akW1rsk_xQBtH4_aXmRk1CI6mZDnPxhdnbrg_CEHclU/export?format=csv'

const profiles = ref([])

function parseCSV(text) {
  const lines = text.trim().split('\n')
  const headers = lines[0].split(',').map(h => h.trim())
  return lines.slice(1).map(line => {
    const values = line.split(',').map(v => v.trim())
    const obj = {}
    headers.forEach((h, i) => {
      obj[h] = values[i]
    })
    return obj
  })
}

onMounted(async () => {
  const res = await fetch(SHEET_CSV_URL)
  const csv = await res.text()
  console.log(csv) // Debugging: log the CSV content
  const data = parseCSV(csv)
  // Map fields to match your template
  profiles.value = data.map(row => ({
    id: row["Current Rank"],
    name: row.Name,
    name_cont: row['Name cont.'],
    country: row.Country,
    birthday: row.Birthday,
    company: row.Company,
    notes: row.Notes,
  }))
  console.log(profiles.value)
})

</script>

<style>
.profiles {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.profile-card {
  width: 120px;
  text-align: center;
}

.profile-img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
}

.profile-name {
  margin-top: 8px;
  font-weight: bold;
}

.profile-detail {
  font-size: 12px;
  color: #666;
}
</style>