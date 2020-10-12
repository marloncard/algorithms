import axios from 'axios';

/*** Coordinate Lookup by Postal Code
 * @param {String} Postal Code
 * Return: Object { lat: <latitude>, lng: <longitude> }
 */
export default async function postalLookup (postalCode) {
  const apiKey = process.env.G_API_KEY;
  const baseUrl = `https://maps.googleapis.com/maps/api/geocode/json?key=${apiKey}&components=postal_code:${postalCode}`;
  return axios.get(baseUrl)
    .then((res) => {return res.data.results[0].geometry.location})
    .catch(err => console.error(err))
}
