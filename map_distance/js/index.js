import postalLookup from './postalLookup.js';
import haversineDistance from './haversine.js';

const destination = [40.964412, -73.838602];

const myDistance = async (pointB) => {
  try {
    const pointA = '10530';
    const {lat, lng} = await postalLookup(pointA);
    const distance = haversineDistance([lat, lng], pointB);
    console.log(distance)
    return distance
  } catch {
    (err) => console.log(err);
  }
}

myDistance(destination);