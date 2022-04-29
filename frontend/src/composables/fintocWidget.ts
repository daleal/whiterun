import { getFintoc } from '@fintoc/fintoc-js';
import { FINTOC_PUBLIC_KEY } from '@/constants';

const fintocPromise = getFintoc();

export const useFintocWidget = async ({
  widgetToken,
  onSuccess = () => null,
  onExit = () => null,
}: {
  widgetToken: string,
  onSuccess?: () => void,
  onExit?: () => void,
}) => {
  const fintoc = await fintocPromise;

  return fintoc?.create({
    widgetToken,
    publicKey: FINTOC_PUBLIC_KEY,
    holderType: 'individual',
    product: 'payments',
    onSuccess,
    onExit,
  }) || null;
};
