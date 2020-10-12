/**
 * Calculate haversine distance between two points
 * @param {number[]} latlng_A [lat1, lng1] Point A
 * @param {number[]} latlng_B [lat2, lng2] Point B
 */
export default function haversineDistance ([lat1, lon1], [lat2, lon2]) {
  const toRadian = angle => (Math.PI / 180) * angle;
  const distance = (a, b) => (Math.PI / 180) * (a - b);
  const EARTH_RADIUS_KM = 6371;

  const dLat = distance(lat2, lat1);
  const dLon = distance(lon2, lon1);

  lat1 = toRadian(lat1);
  lat2 = toRadian(lat2);

  // Haversine Formula
  const a =
  Math.pow(Math.sin(dLat / 2), 2) +
  Math.pow(Math.sin(dLon / 2), 2) * Math.cos(lat1) * Math.cos(lat2);
  const c = 2 * Math.asin(Math.sqrt(a));

  let finalDistance = EARTH_RADIUS_KM * c;

  // Convert to miles
  finalDistance /= 1.60934;
// console.log(finalDistance);
return finalDistance;
};